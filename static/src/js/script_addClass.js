// $(document).ready(function(){
  // // $("#myTablei tbody").on('mousedown', 'tr', function(){
	  // // console.log('here!!')
    // // $("#conductor").addClass("module");
  // // },function(){
		// // $("#conductor").removeClass("module");
	// // }
	// // );
  // // $("#ball").mousemove(function(e){
	 // // if(e.which==1)
	 // // {
	   // // $("#conductor").toggleClass("module");
	 // // }
  // // });
	
	
	// var clicked = false;
	
	// //if clicked on table row - clicked true, module class added
	// $("#myTablei tbody").on('mousedown','tr', function(){
			// //check if row is already selected
			// var testSelected = $(this).hasClass("selected");
			// if(testSelected){
				// //if yes add class module and clicked = true
				// //$("#conductor").addClass("module");
				// clicked = true;
				// //are you hovering over droppable div?
				// //yes add color to droppable div
				// //code extracted from github.com/kchiran
				// //from javascript.info/mouseover
				// //let currentDroppable = null;
				
				// let currentDroppable = null;
				// myULi.onmouseover = function() {
					// if (currentDroppable) return;
					// let target = event.target.closest('li');
					// if (!target) return;
					// if (!myULi.contains(target)) return;
					// currentDroppable = target;
					// onEnter(currentDroppable);
					// //console.log('111')
				// };
				// myULi.onmouseout = function(event) {
					// if (!currentDroppable) return;
					// let relatedTarget = event.relatedTarget;
					// while (relatedTarget) {
						// if (relatedTarget == currentDroppable) return;
						// relatedTarget = relatedTarget.parentNode;
					// }
					// onLeave(currentDroppable);
					// currentDroppable = null;
				// };
				// function onEnter(elem) {
				// elem.style.background = 'pink';
				// }
				// function onLeave(elem) {
				// elem.style.background = '';
				// }
				
				// /*myULi.onmouseenter = function(event) {
				// let target = event.target;
				// target.style.background = 'pink';
				// };

				// myULi.onmouseleave = function(event) {
				// let target = event.target;
				// target.style.background = '';
				// };*/
				// };

				// });
	
	// //if mouseup on body anywhere - check if clicked true and unset
	// $(document).on('mouseup', function(){
		// if (clicked) {
			
			// //is this over a droppable div?
			// //var newListItem = document.createElement("li");  
			// //if yes put alert database updated
			
			// clicked = false;
			// $("#conductor").removeClass("module");
		// }
	// });
	
	// // if ($( "#myDiv2" ).hasClass(( "drag.even.selected" ) || ("drag.odd.selected"))){
		// // //console.log(this)
	// // }
		
	
// });
random = Math.random()

//Onclick call this function + modal open simultaniously
	
function imgGalleryAjax(){
	random = Math.random()
	odoo.define('web.ajax'+random, function(require){
		'use strict';
		var ajax =require ('web.ajax');
			//Pass the value in the textbox
			var textBox1 = $('input[name="textBox1"]').val()
			//var prod_id = $('input[name="textBox2"]').val()
			var prod_id = $('input[name="textBox2"]').val()
			//console.log(prod_id)
		
			// call the python function through ajax from specifying the route
			var res = ajax.jsonRpc("/pcm/products/browse/"+prod_id, 'call', {
						'textBox1': textBox1,
						'textBox2': prod_id

			}).then(function(returnval){
				returnval = JSON.parse(returnval);
				
				if(returnval['status'] == 'OK'){
					//return value was successful
					//format and paste html into modal
					document.getElementById("image1").src = "/product_shelf/static/src/img/"+prod_id+"/1.png";
					document.getElementById("image2").src = "/product_shelf/static/src/img/"+prod_id+"/2.png";
					document.getElementById("image3").src = "/product_shelf/static/src/img/"+prod_id+"/3.png";
					document.getElementById("image4").src = "/product_shelf/static/src/img/"+prod_id+"/4.png";
					document.getElementById("image5").src = "/product_shelf/static/src/img/"+prod_id+"/5.png";
					document.getElementById("image6").src = "/product_shelf/static/src/img/"+prod_id+"/6.png";
				}
			})
	})
}

var modal='#myModal2';
//console.log("Modal Close!!!")
$(document).on('hidden.bs.modal', function (e) {
	if (e.target.id === 'myModal2')
	//do stuff
	//var id = $('#textBox2').val()
	//console.log("Modal Close!!!");
	$(".drag").removeClass("selected");
	$(".gallery").removeClass("choose");
	$("#textBox2").val("");
	$("#textBox1").val("");
	$(".image").attr("src", "/product_shelf/static/src/img/load.gif");
	//$("#"+prod_id+ "td img src").attr("src", "/product_shelf/static/src/img/load.gif");
});

function uploadImgAjax(){
	random = Math.random()
	odoo.define('web.ajax1'+random, function(require){
	'use strict';
	var ajax = require('web.ajax');

		//get value of items defined as variable in python
		var idy = $('input[name="textBox2"]').val()
		var f_names = $('input[name="textBox1"]').val()
		console.log(f_names)

		// call the python function through ajax from specifying the route
		var res = ajax.jsonRpc("/pcm/update/images/"+idy, 'call', {
			'idy': idy,
			'f_names': f_names
		}).then(function(returnval){
			returnval = JSON.parse(returnval);
			if(returnval['status'] == 'OK'){
				//return value was successful
				//format and paste html into modal
				console.log($("#"+idy));
				console.log($("#"+idy+ " td"));
				console.log($("#"+idy+ " td img"));
				$("#"+idy+ " td img").attr("src", "/product_shelf/static/src/img/"+idy+"/" +f_names[0]+ ".png");
			}
		})
	})
}

function catCreatAjax(){
	random = Math.random()
	odoo.define('we.ajax2'+random, function(require){
	'use.strict';
	var ajax = require('web.ajax');

		//get the values clicked item or pass them in
		var idx = $("#_id").val()
		//var idx = $("#fieldid").val()
		var name = $("#cat_Txt").val()
		var complete_name =$("#par_cat").val() +" / "+ name
		var parent_path =$("#par_path").val()

		//call the function through ajax from routing
		var res = ajax.jsonRpc("/pcm/category/"+idx, "call", {
			'idx':idx,
			'name':name,
			'complete_name':complete_name,
			'parent_path':parent_path,
		}).then(function(returnval){
			returnval = JSON.parse(returnval);
			if (returnval["status"]=="OK"){
				//return value was successful
				//format and paste html onto the modal or anywhere concerned
				var idi = returnval["idi"]

				if ($('#'+idx +'ul:last')) {

					$("#"+idx).append("<ul><a id="+idi+"><div class='dropabble'>"+name+"</div></a></ul>");
					document.getElementById(idi).href="/pcm/products"+"/"+idi

				} else {
					
					$('#'+idx +'ul:last').after("<ul><a id="+idi+"><div class='dropabble'>"+name+"</div></a></ul>");
					document.getElementById(idi).href="/pcm/products"+"/"+idi

				}
				console.log($("#"+idx))
			}
		})
	})
}
function catDropAjax(){
	random = Math.random()
	//if (confirm('Are you sure you want to delete this category from  the database?')) {
		// Save it!
		//console.log('Thing was saved to the database.');
	  
		odoo.define('web.ajax3'+random, function(require){
		'use.strict';
		//else {
			// Do nothing!
			//console.log('Thing was not saved to the database.');
		// }
		var ajax = require('web.ajax');
			//get the values of the items on click or pass them in 
			var idw = $("#_id").val()
			//var alfa = 0;
			var beta = document.getElementById(idw).innerText;
			// call the function through ajax from routing
			var res = ajax.jsonRpc("/pcm/delete/"+idw, "call", {
				'idw': idw,

			}).then(function(returnval){

				returnval = JSON.parse(returnval);
				var zoop = returnval['zoop'];
				//console.log(returnval);
				//var zoop = document.getElementById('myTablei_info').innerText;
				//zoop = zoop.split(" ")[5];
				console.log(zoop);
				if (returnval['status']=='OK') {
					
					//return value was successful
					//format or alter the html content of the site to reveal the success of the function
					//alert box to warn the user regarding foreign key constraint violation
					if (confirm('Are you sure you want to delete this category from  the database?')) {
						$("#"+idw).remove();
					}
					
				}
				else {
					//window.alert('Sorry you cannot delete this category because it violates the foreign key constraint!')
					//var zoop = returnval['zoop'];
					if (confirm('Do you want to delete ' +zoop+ ' products in '+beta+' as well?')){
						//console.log("Let's clear all the products as well!!")
						al_prod_delete(idw)
						//if confirmed we'll post the value 1 that will run the script that can delete all the products inside that category
					}
				}

			})
		})
	//}
}
// function fetchAjax2(){
// 	random=Math.random()
// 	odoo.define('web.ajax4'+random, function(require){
// 		'use.strict';
// 		//console.log("Look!!");
// 		//var ajax = require('web.ajax');
// 		//toggle the class first
// 		//var menu = document.querySelector('.nav-link')
// 		//console.log(menu);
// 		//menu.classList.toggle('active');
// 		//$('#btn-1).toggleClass('active');
// 		//then load the data
// 		var div = document.getElementById('aria_div_desc')
// 		div.innerHTML += ("Lorem ipsum dolor sitad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis");
		
// 	})
// }

// $(document).ready(function(){
// 	//$('#btn-1').addClass("active");
// 	$(".nav-link").click(function(){
// 	  $(this).toggleClass("active");
// 	});
//   });
function al_prod_delete(idk){

	random = Math.random()

	odoo.define ('web.ajax77'+random, function(require){
		'use.strict';
		var ajax = require('web.ajax');
		var kap = $("#_id").val();

		//get the values to put into python

		var res = ajax.jsonRpc("/pcm/prodel/"+idk, "call", {
			'idk':idk
		}).then(function(returnval){

			returnval = JSON.parse(returnval);

			if(returnval['status'] == 'OK'){
				//return value was successfull
				//parse it into the HTML
				$(".drag").remove();
				$("#"+kap).remove();

			} else if (returnval['status'] == 'tamam') {

				$(".drag").remove();
				$("#"+kap).remove();
				window.alert("All Cleared!");

			}

			else {

				window.alert("Sorry you cannot perform this operation!");
			}
			 
		})
	})
}
