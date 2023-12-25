import Cookies from 'js-cookie';

export function setDefaultCoordinates() {
  const defaultCoordinates = [
    { latitude: 56.0, longitude: 10.0 },
    { latitude: 57.0, longitude: 11.0 },
    { latitude: 56.0, longitude: 10.0 },
    { latitude: 57.0, longitude: 11.0 }
  ];
  Cookies.set('coordinates', JSON.stringify(defaultCoordinates));
}
