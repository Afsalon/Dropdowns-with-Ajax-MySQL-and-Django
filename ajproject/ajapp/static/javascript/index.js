document.getElementById('form1').addEventListener('submit',getStateData);
var v =''
function getStateData(e){
  e.preventDefault();
  v = document.getElementById('country_button').value;
  var xhr = new XMLHttpRequest();
  xhr.open('GET','http://127.0.0.1:8000/country/'+v,true);
  xhr.onload = function(){
    if( this.status == 200){
      output = ''
      var statedata = JSON.parse(this.responseText);
      // console.log(statedata);
      for (i in statedata){
        output += '<option id="'+statedata[i].name+'" value="'+statedata[i].id+'">'+statedata[i].name+'</option>'
      }
      document.getElementById('state_button').innerHTML = output
    }
  }
  xhr.send();
}

document.getElementById('form2').addEventListener('submit',getCityData);

function getCityData(e){
  e.preventDefault();
  var g = document.getElementById('state_button').value;
  var vhr = new XMLHttpRequest();
  vhr.open('GET','http://127.0.0.1:8000/country/'+v+'/'+g+'/',true);
  vhr.onload = function(){
    if( this.status == 200){
      output = ''
      var citydata = JSON.parse(this.responseText);
      // console.log(citydata);
      for (i in citydata){
        output += '<option id="'+citydata[i].name+'" value="'+citydata[i].name+'">'+citydata[i].name+'</option>'
      }
      document.getElementById('city_button').innerHTML = output
    }
  }
  vhr.send();
}


document.getElementById('form3').addEventListener('submit',dosomerefreshing);
function dosomerefreshing(e){
  e.preventDefault();
  window.scroll({
  top: 2500,
  left: 0,
  behavior: 'smooth'
})
};
