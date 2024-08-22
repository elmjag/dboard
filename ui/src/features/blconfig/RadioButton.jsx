import Form from 'react-bootstrap/Form';

function RadioButton({name, selected, onChange})
{
  const lowerCaseName = name.toLowerCase();

  let isChecked = selected.toLowerCase() === lowerCaseName;

  return (
    <div key="radio" className="mb-3">
      <Form.Check type="radio">
      <Form.Check.Input type="radio" checked={isChecked} onChange={() => onChange(lowerCaseName)}/>
      <Form.Check.Label>{name}</Form.Check.Label>
      </Form.Check>
    </div>
  );
}

export default RadioButton;
