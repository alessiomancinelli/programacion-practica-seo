const axios = require['axios'];
const jsdom = require['jsdom'];



//Request - ora fare richiesta
//const response = axios.get('https://seohacks.es');
//console.log(response);


async function fetch(url) {
    const response = await axios.get(url);
    console.log(response);

}

fetch('https://seohacks.es');


//Parsing


//Output

