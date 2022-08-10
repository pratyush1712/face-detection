import './App.css';
import { Container, Typography, Grid } from "@mui/material";

//----------------------------------------------------------
const developmentTechnologies = ['Flask', 'React', 'Heroku', 'God, I hate deployement']
const functioningTechnologies = ['OpenCV', 'Coroutines', 'Haar Cascades']

function App() {
  return (
    <Container sx={{ p: 3, display: 'flex', flexDirection: 'column' }} align={'center'}>
      <Typography variant='h5' my={3} component='button' borderRadius={2} p={1.6} width={'60%'} sx={{ mx: 'auto' }}>Face and Eyes Detection Application</Typography><br />
      <img src={'/video'} alt={'face and eyes detected'} style={{ borderRadius: 12, padding: 5, border: '1px solid #ddd', width: '40vw', margin: 'auto', align: 'center', justifyContent: 'center', }} />
      <Typography variant='subtitle1' component='button' borderRadius={2} p={1} mt={3} width={'50%'} sx={{ mx: 'auto' }}>Technologies Used</Typography>
      <Grid container p={1}>
        <Grid item xs={12} md={6}>
          <Typography variant='subtitle2' component='button' borderRadius={2} p={0.8}>Development Technologies</Typography>
          <Grid container spacing={1} mt={0.2} justifyContent={'center'} mb={5}>
            {developmentTechnologies.map(tech => (
              <Grid item>
                <Typography variant='caption' component='button' borderRadius={8} p={0.8}>{tech}</Typography>
              </Grid>
            ))}
          </Grid>
        </Grid>
        <Grid item xs={12} md={6}>
          <Typography variant='subtitle2' component='button' borderRadius={2} p={0.8}>Backend Functionality</Typography>
          <Grid container spacing={1} mt={0.2} justifyContent={'center'} mb={5}>
            {functioningTechnologies.map(tech => (
              <Grid item>
                <Typography variant='caption' component='button' borderRadius={8} p={0.8}>{tech}</Typography>
              </Grid>
            ))}
          </Grid>
        </Grid>
      </Grid>
    </Container>
  );
}

export default App;
