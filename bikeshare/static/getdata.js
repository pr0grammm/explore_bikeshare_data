mytable=document.getElementById("tbl");//keep adding to end of this element
clearbtn = window.parent.document.getElementById("clearbtn");
morebtn = window.parent.document.getElementById("morebtn");


var url = "/gimmeHTML/";//URL which outputs html of 5 more rows
var start =0;

clearbtn.addEventListener("click", cleartable);
morebtn.addEventListener("click", showmore);


function cleartable(){
	mytable.innerHTML ='';

};

function showmore(){
	start =start+5;//first 5 rows already present
	var ourRequest = new XMLHttpRequest(); //tool for asynchronous requests
	ourRequest.open('GET', url+start);
	ourRequest.onload = function(){
		html=ourRequest.responseText;
		renderHTML(html);
		window.scrollTo(0,window.scrollMaxY)
	};
	
	ourRequest.send();
};

function renderHTML(html){
mytable.insertAdjacentHTML("beforeend", html)
}