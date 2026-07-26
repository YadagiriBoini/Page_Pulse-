async function analyze(){

let url=document.getElementById("url").value;

let result=document.getElementById("result");

result.innerHTML="Analyzing...";

let response=await fetch("/analyze",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({url:url})

});

let data=await response.json();

if(data.error){

result.innerHTML="<p>"+data.error+"</p>";

return;

}

result.innerHTML=`

<h3>Report</h3>

<p><b>HTTP Status:</b> ${data.status}</p>

<p><b>Response Time:</b> ${data.response_time}</p>

<p><b>Title:</b> ${data.title}</p>

<p><b>Meta Description:</b> ${data.description}</p>

<p><b>H1 Count:</b> ${data.h1_count}</p>

<p><b>Images Missing Alt:</b> ${data.missing_alt}</p>

<p><b>Word Count:</b> ${data.word_count}</p>

`;

}