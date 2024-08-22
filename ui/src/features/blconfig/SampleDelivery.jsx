import RadioButton from './RadioButton'
import { useSelector, useDispatch } from 'react-redux'
import { setSampleDelivery } from './blconfigSlice'
import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';

export function SampleDelivery()
{
  const selectedSampleDelivery = useSelector((state) => state.blconfig.sampleDelivery);
  const dispatch = useDispatch();

  function onChange(name)
  {
    dispatch(setSampleDelivery(name));
  }

  return (
    <Card>
      <Card.Body>
        <Card.Title>Sample Delivery</Card.Title>
        <Form>
          <RadioButton name="OSC" selected={selectedSampleDelivery} onChange={onChange}/>
          <RadioButton name="HVE" selected={selectedSampleDelivery} onChange={onChange}/>
        </Form>
      </Card.Body>
    </Card>

  );
}
