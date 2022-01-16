function myFunction(){
    console.log("HELLO");
    var holder= document.getElementById("equation").value;
    let data = {diffEquation: holder};
    

    // fetch("http://127.0.0.1:5000/", {
    // method: "POST",
    // headers: {'Content-Type': 'application/json'}, 
    // body: JSON.stringify(data)
    // }).then(res => {
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/",
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
//     var tr_str =
              
//             '<td>'+
//         '<div class="card" style="width: 250px;">' +
//         '<p>'+res+' </p>'+        
//         '</input>' +
//         ' </a>' +
    
//         ' </div>' +
//             '</div>'+
//             '</td>'   
//             ;
    
//     //append the variable to the dom element
// document.getElementById("info").innerHTML += tr_str;
});
}




const value = document.getElementById('equation');
let buttons = Array.from(document.getElementsByClassName('button'));

buttons.map( button => {
    button.addEventListener('click', (e) => {
        switch(e.target.innerText){
            case 'x':
                equation.innerText ='x';
                break;
            case '=':
               console.log(display.innerText);
                try{
                    if(equation.innerText.includes("Math.pow")){
                        equation.innerText=eval(equation.innerText);
                    }
                    if(equation.innerText.includes("∧") ||equation.innerText.includes("∨")){
                        var str =equation.innerText;
                        while(str.includes('∧')){
                            str= str.replace('∧','&');
                        }
                        while(str.includes('∨')){
                            str= str.replace('∨','||');
                        }
                        console.log(str);
                        console.log(eval(str));
                        equation.innerText="";
                        equation.innerText = eval(str);
                        break;
                    }

                    if(equation.innerText.includes("∫")){
                        try{
                            let array=equation.innerText.split(',');
                            var str=array[0].substring(1);
                            var beg=array[1];
                            var end=array[2];
                            console.log(end);
                            equation.innerText=integrate(str,beg,end);
                        }catch{
                            equation.innerText = "Error Value"
                        }
                        break;
                    }
                    else{
                        equation.innerText = eval(equation.innerText);
                    }

                } catch {
                    equation.innerText = "Error"
                }
                break;
            case '←':
                if (equation.innerText){
                    equation.innerText = equation.innerText.slice(0, -1);
                }
                break;
            case 'Integral Help':                        
                equation.innerText="For using ∫, type ∫(function),beg,end bounds";
                    break;
            default:
                equation.innerText += e.target.innerText;
                
        }
    });
    document.addEventListener('keydown', function(event) {
        switch(event.keyCode){
            case 'x':
                equation.innerText ='x';
                
                break;
            case '=':
               console.log(equation.innerText);
                try{
                    if(equation.innerText.includes("∧") ||equation.innerText.includes("∨")){
                        var str =equation.innerText;
                        if(equation.innerText.includes("∧")){
                            str= str.replace("∧","&&");
                        }
                        if(equation.innerText.includes("∨")){
                            str= str.replace("∨","||");
                        }
                        
                        equation.innerText = eval(str);
                    }
                   
                    if(equation.innerText.includes("∫")){
                        try{
                            let array=display.innerText.split(',');
                            var str=array[0].substring(1);
                            var beg=array[1];
                            var end=array[2];
                            console.log(end);
                            equation.innerText=integrate(str,beg,end);
                        }catch{
                            equation.innerText = "Error Value"
                        }
                    }
                    else{
                        equation.innerText += eval(equation.innerText);
                    }

                } catch {
                    equation.innerText = "Error"
                }
                break;
            case '←':
                if (equation.innerText){
                    equation.innerText = display.innerText.slice(0, -1);
                }
                break;
            default:
                equation.innerText += e.target.innerText;
                
        }
    });

});

function valueAt(fun,val){
    try{
        while(fun.includes('x')==true){
            fun=fun.replace("x",val);
        }
        return eval(fun);
    }
    catch{
        display.innerText="ERROR CHECK";
        return -1;
    }    
}