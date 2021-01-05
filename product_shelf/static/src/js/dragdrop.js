$(document).ready(function(id, idx, man_code){
	// JAVASCRIPT (jQuery)
	//console.log("I'm here!!");
	var id;
	var idx;
	var man_code;
	// Trigger action when the contexmenu is about to be shown
	$(".drag").bind("contextmenu", function (event) {
		id = $( this ).attr("id");
		console.log("ID: "+id);
		$("#textBox2").val(id)
		$("#"+id ).toggleClass("selected");
		man_code = $(this).closest("tr").find('td:eq(2)').text();
		console.log("Manufacturer's Code: "+man_code);
		event.preventDefault();
		// Show contextmenu
		$(".custom-menu").finish().toggle(100).
		
		// In the right position (the mouse)
		css({
			top: event.pageY + "px",
			left: event.pageX + "px"
		});
		
	});
	// If the document is clicked somewhere
	$(document).bind("mousedown", function (e) {
		// If the clicked element is not the menu
		if (!$(e.target).parents(".custom-menu").length > 0) {
			// Hide it
			$(".custom-menu").hide(100);
		}
	});
	// If the menu element is clicked
	$(".custom-menu li").click(function(){
		//console.log(this);
		console.log("I got an "+id)
		// This is the triggered action name
		switch($(this).attr("data-action")) {
			// A case for each action. Your actions here
			case "first":; break;
			case "second":; break;
			case "third":; break;
			case "fourth":; break;
			case "fifth":; break;
		}
		// Hide it AFTER the action was triggered
		$(".custom-menu").hide(100);
	  });
	
	//The part from down here is for right-click of nodes implementation
	//----------------------------------------------------------------------------------------------------------------------------------------------------
	//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	//-----------------------------------------------------------------------------------------------------------------------------------------------------
	// Trigger action when the contexmenu is about to be shown
	$(".droppable").bind("contextmenu", function (event) {
		idx = $( this ).parent($("a")).attr("id");
		console.log("_ID " +  $( this ).parent($("a")).attr("id"))
		$("#_id").val(idx);
		$(this).toggleClass("selected");
		//$("#par_path").val($( this ).parent($("a")).attr("id"));
		//alert($( this ).text());
		$("#par_path").val($( this ).parent($("a")).attr("path"));
		$("#par_cat").val($( this ).parent($("a")).attr("cname"));
		//$("#par_path").val($( this ).text().trim() + "");
		//console.log(this);
		//console.log("_ID: "+idx);
		//$("#"+idx ).child($("div")).toggleClass("selected");
		//man_code = $(this).closest("tr").find('td:eq(2)').text();
		//console.log("Manufacturer's Code: "+man_code);
		event.preventDefault();
		// Show contextmenu
		$(".custom-menu-drop").finish().toggle(100).
		// In the right position (the mouse)
		css({
			top: event.pageY + "px",
			left: event.pageX + "px"
		});
	});
	// If the document is clicked somewhere
	$(document).bind("mousedown", function (e) {
		// If the clicked element is not the menu
		if (!$(e.target).parents(".custom-menu-drop").length > 0) {
			// Hide it
			$(".custom-menu-drop").hide(100);
		}
	});
	// If the menu element is clicked
	$(".custom-menu-drop li").click(function(){
		//console.log(this);
		console.log("I got an "+idx)
		// This is the triggered action name
		switch($(this).attr("data-action")) {
			// A case for each action. Your actions here
			//case "first": location.href="/pcm/category/"+idx; break;
			case "first":; break;
			case "second":; break;
			case "third":; break;
			case "fourth":; break;
		}
		// Hide it AFTER the action was triggered
		$(".custom-menu").hide(100);
	  });
	
});