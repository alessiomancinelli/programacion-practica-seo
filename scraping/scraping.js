const axios = require['axios'];
const jsdom = require['jsdom'];

//const { JSDOM } = jsdom;



const response = axios.get('https://www.hotelleria.it');
console.log(response);


//async function scrape(url) {
    //Request - ora fare richiesta

    //const response = await axios.get(url);
    //console.log(response);

    //Parsing

    //const dom = new JSDOM(response.data);
    //console.log(dom);

    //Output

    //const title = dom.window.document.querySelector('title');

    //console.log(title)

//}

//scrape('https://seohacks.es');




//Output

