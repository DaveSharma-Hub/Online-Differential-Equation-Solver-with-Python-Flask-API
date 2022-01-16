function myFunction(){
    console.log("HELLO");
    var holder= document.getElementById("equation").value;
    let data = {diffEquation: holder};
    

        $.ajax({
            type: "POST",
            url: "localhost:5000/",
            data: holder, // <-- Put comma here
            contentType: 'text/plain'
        }).then(res=>{ 
        console.log("Request complete! response:", res);
        
        $(document).ajaxComplete(function() {
            
            var $label = $("#info");
            var text = $label.text();
            var tmp =res.replaceAll("**","^");
            $label.text(text.replace(text, tmp)); 
        });

});
}
