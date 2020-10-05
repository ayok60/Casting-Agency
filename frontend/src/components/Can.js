
const token = localStorage.getItem('JWTS_LOCAL_KEY');

const parseJwt = (token) => {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
    return JSON.parse(jsonPayload);
  };

const check = (permission) => {

    const payload = parseJwt(token);
    console.log(permission);
    console.log(payload && payload.permissions && payload.permissions.length && payload.permissions.indexOf(permission) >= 0);
    return (payload && payload.permissions && payload.permissions.length && payload.permissions.indexOf(permission) >= 0);
};

const Can = props =>
  check(props.permission)
    ? props.yes()
    : props.no();

Can.defaultProps = {
  yes: () => null,
  no: () => null
};

export default Can;