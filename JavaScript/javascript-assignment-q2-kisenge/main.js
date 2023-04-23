var names= ["Ed","Jo","Rose","Katie","David"];
var names2=[];
var durations=[4000, 5000, 10000, 6500,2500];
var durations2=[];
var name;
var duration;


function haircut(names,durations){

  var  inc=0;
  var returnInc=0;
  if(names.length>0 ){
    while(names.length>0){
      name=names.pop();
      names2[inc]=name;
      duration=durations.pop();
      durations2[inc]=duration;
      inc= inc+1;
    }

    for (let i = 0; i <inc; i++) {
      console.log("Starting to cut "+names2[i]+ "'s hair'");
    }

    for (let i = 0; i <inc; i++) {
      setTimeout(function() {returnCut(names2[i]);},durations2[i]);
    }

    //setTimeout(function() {haircut(names,durations);},duration);

    function returnCut(name){
      //haircut(names,durations);
      console.log(name+" has a brand-new haircut!");
      if(returnInc==inc-1){
        console.log("All haircuts are done now!");
      }
      returnInc= returnInc+1;
    }
  }




}



let promise1 = new Promise((resolve, reject) => {

  // Do stuff
  if(haircut(names,durations)){
    resolve([names,durations]);
  }

  else {
    reject(Error('There is problem'));
  }
});

promise1.then(
  function(names,durations) {haircut(names,durations);},
  function(error) {console.log("This is an error");}
);
