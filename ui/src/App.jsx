import Dashboard from './Dashboard.jsx'
import { useEffect } from 'react';
import { useDispatch } from 'react-redux'
import { setCompleteConfiguration } from './features/blconfig/blconfigSlice'
import { Container, Row, Col } from 'react-bootstrap';

async function FetchBeamlineConfig(dispatch)
{
  const response = await fetch("/api/config");
  if (!response.ok)
  {
    throw new Error(`Response status: ${response.status}`);
  }

  const json = await response.json();
  dispatch(setCompleteConfiguration(json));
}

function App()
{
  const dispatch = useDispatch();

  useEffect(() =>
  {
    FetchBeamlineConfig(dispatch).catch(console.error);
  });

  return (
    <Container fluid className="d-flex vh-100">
      <Row className="m-auto">
        <Col className="text-center">
          <Dashboard/>
        </Col>
      </Row>
    </Container>
  );
}

export default App;
