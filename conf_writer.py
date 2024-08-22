import logging
from pathlib import Path
from shutil import copyfile
from template_context import generate_template_context

log = logging.getLogger(__name__)

TEMPLATES_DIR = Path("micromax-templates")
TEMPLATE_SUFFIX = "-template"


def _walk_dir(root: Path):

    for node in root.iterdir():
        if node.is_dir():
            for child in _walk_dir(node):
                yield child
            continue

        yield node


def _get_source_files():
    return _walk_dir(TEMPLATES_DIR)


def _is_template_file(file: Path):
    fname = file.name.lower()
    return fname.endswith(TEMPLATE_SUFFIX)


def _get_templates_result_path(template_file: Path):
    result_filename = template_file.name[: -len(TEMPLATE_SUFFIX)]
    return Path(template_file.parent, result_filename)


def _get_destination_path(mxcube_conf_dir: Path, source_path: Path) -> Path:
    # rebase template path onto MXCuBE configs directory
    return Path(mxcube_conf_dir, source_path.relative_to(TEMPLATES_DIR))


def _process_template(template_file: Path, template_context: dict):
    template_text = template_file.read_text()
    return template_text.format(**template_context)


def _write_templated_config_file(
    mxcube_conf_dir: Path, source_file: Path, template_context: dict
):
    template_path = _get_templates_result_path(source_file)
    template_text = _process_template(source_file, template_context)

    destination_path = _get_destination_path(mxcube_conf_dir, template_path)

    _write_config_file(destination_path, text=template_text)

    destination_path.write_text(template_text)


def _write_config_file(
    destination: Path, source: Path | None = None, text: str | None = None
):
    destination.parent.mkdir(parents=True, exist_ok=True)

    if text is None:
        # we are just copy as-is, use the (possibly) fast copy operation
        copyfile(source, destination)
    else:
        destination.write_text(text)

    log.info(f"wrote '{destination}'")


def write_config_files(mxcube_conf_dir: Path, beamline_setup):
    log.info(f"writing MXCuBE configuration files to '{mxcube_conf_dir}'")
    log.info(f"specified beamline setup\n{beamline_setup}")

    template_ctx = generate_template_context(beamline_setup)

    for source_file in _get_source_files():
        if _is_template_file(source_file):
            _write_templated_config_file(mxcube_conf_dir, source_file, template_ctx)
        else:
            destination_path = _get_destination_path(mxcube_conf_dir, source_file)
            _write_config_file(destination_path, source_file)

    log.info("finished writing MXCuBE configurations files")
