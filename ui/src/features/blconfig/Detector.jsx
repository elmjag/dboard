import RadioButton from './RadioButton'
import { useSelector, useDispatch } from 'react-redux'
import { setDetector } from './blconfigSlice'
import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';

export function Detector()
{
  const selectedDetector = useSelector((state) => state.blconfig.detector);
  const dispatch = useDispatch();

  function onChange(name)
  {
    dispatch(setDetector(name));
  }

  return (
    <Card>
      <Card.Body>
        <Card.Title>Detector</Card.Title>
        <Form>
          <RadioButton name="Eiger" selected={selectedDetector} onChange={onChange}/>
          <RadioButton name="Jungfrau" selected={selectedDetector} onChange={onChange}/>
        </Form>
      </Card.Body>
    </Card>
  );
}
