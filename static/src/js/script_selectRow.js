$(document).ready(function() {
    var table = $('#myTablei').DataTable();
 
    $('#myTablei tbody').on( 'click', 'tr', function () {
        $(this).toggleClass('selected');
		prev_val = $("#fieldid").val()
				//if (prev_val==null){
					if(prev_val.includes($( this ).attr("id")+";")){
						prev_val = prev_val.replace($( this ).attr("id")+";","")
						$("#fieldid").val(prev_val)
					}
					else
						$("#fieldid").val($("#fieldid").val() + $( this ).attr("id")+";")
    } );
 
   // $('#button').click( function () {
    //    alert( table.rows('.selected').data().length +' row(s) selected' );
   // } );
} );
