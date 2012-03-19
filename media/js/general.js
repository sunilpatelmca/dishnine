
this.easyscroll = function(){
	
	// id of the container element 
	//var id = "myContent";
	
	// navigation buttons text
	//var nav = ["Scroll Up", "Scroll Down", "Reset"];
	
	//	id for each navigation button (OPTIONAL)
	//var navId = ["btnUp", "btnDown", "btnReset"];

	// movement speed
	var speed = 1;
	
	// desired height of the container element (in pixels)
	
	if(document.getElementById('myContent')){
		var obj = document.getElementById('myContent');
		var height = 252;	}
	else if(document.getElementById('myTableContent')){
		var obj = document.getElementById('myTableContent');
		var height = 335; }
	
	//
	// END CONFIG
	// do not edit below this line (unless you want to of course :) )
	//

	
	var arrow_up_obj = document.getElementById("arrow_up");
	var arrow_down_obj = document.getElementById("arrow_down");
	
	obj.up = false;
	obj.down = false;
	obj.fast = false;

	var container = document.createElement("div");
	var parent = obj.parentNode;
	container.id="easyscroll";
	parent.insertBefore(container,obj);
	parent.removeChild(obj);	
	
	container.style.position = "relative";
	container.style.height = height;
	container.style.overflow = "hidden";
	obj.style.position = "absolute";
	obj.style.top = "0";
	obj.style.left = "0";
	obj.style.width = "100%";
	container.appendChild(obj);
	
	//var btns = new Array();
	//var ul = document.createElement("ul");
	//ul.id="easyscrollnav";
	//for (var i=0;i<nav.length;i++){
//		var li = document.createElement("li");
//		li.innerHTML = nav[i];
//		li.id = navId[i];
//		btns.push(li);
//		ul.appendChild(li);
//	};
//	parent.insertBefore(ul,container);
	
	arrow_up_obj.onmouseover = function(){
			
		obj.up = true;
		this.className = "over";
	};
	arrow_up_obj.onmouseout = function(){
		obj.up = false;
		this.className = "";
	};		
	arrow_down_obj.onmouseover = function(){
		obj.down = true;
		this.className = "over";		
	};
	arrow_down_obj.onmouseout = function(){
		obj.down = false;
		this.className = "";
	};		
	arrow_up_obj.onmousedown = arrow_down_obj.onmousedown = function(){
		obj.fast = true;
	};	
	arrow_up_obj.onmouseup = arrow_down_obj.onmouseup = function(){
		obj.fast = false;
	};		
//	btns[2].onmouseover = function(){ 		
//		this.className = "over";
//	};	
//	btns[2].onmouseout = function(){ 		
//		this.className = "";
//	};		
//	btns[2].onclick = function(){ 		
//		obj.style.top = "0px";
//	};		
		
	this.start = function(){				
		var newTop;
		var objHeight = obj.offsetHeight;
		var top = obj.offsetTop;
		var fast = (obj.fast) ? 2 : 1;
		if(obj.down){		 
			newTop = ((objHeight+top) > height) ? top-(speed*fast) : top;	
			obj.style.top = newTop + "px";
		};	
		if(obj.up){		 
			newTop = (top < 0) ? top+(speed*fast) : top;
			obj.style.top = newTop + "px";
		};
	};	
	obj.interval = setInterval("start()",50);		
		
};


//
// script initiates on page load. 
//

this.addEvent = function(obj,type,fn){
	if(obj.attachEvent){
		obj['e'+type+fn] = fn;
		obj[type+fn] = function(){obj['e'+type+fn](window.event );}
		obj.attachEvent('on'+type, obj[type+fn]);
	} else {
		obj.addEventListener(type,fn,false);
	};
};
addEvent(window,"load",easyscroll);

