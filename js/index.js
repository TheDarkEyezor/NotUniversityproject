
function datacollection() {

let url = 'https://api.covid19api.com/summary';
fetch(url)
.then(res => res.json())
.then((out) => {
  console.log('Checkout this JSON! ', out);
})
.catch(err => { throw err });

}


datacollection();