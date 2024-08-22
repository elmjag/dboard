import { useContext } from 'react'
import { ReactReduxContext } from 'react-redux'
import Button from 'react-bootstrap/Button';
import { Detector } from './features/blconfig/Detector.jsx'
import { SampleDelivery } from './features/blconfig/SampleDelivery.jsx'

async function SaveBeamlineConfig(beamlineConfig)
{
  const bodyDict = {
    "sampleDelivery": beamlineConfig.sampleDelivery,
    "detector": beamlineConfig.detector,
  };

  /* TODO: check that we got '200 ok' response */
  await fetch("/api/config", {
    method: "POST",
    headers: { "Content-Type": "application/json", },
    body: JSON.stringify(bodyDict),
  });
}

function ApplyChanges()
{
  const { store } = useContext(ReactReduxContext);

  function onClick()
  {
    const beamlineConfig = store.getState().blconfig;
    SaveBeamlineConfig(beamlineConfig).catch(console.error);
  }

  return (
    <Button onClick={onClick}>apply changes</Button>
  );
}

function Dashboard()
{
  return (
    <>
      <h1>MicroMAX Beamline Setup</h1>
      <Detector/>
      <SampleDelivery/>
      <ApplyChanges/>
    </>
  );
}

export default Dashboard;
