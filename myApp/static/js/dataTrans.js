$.ajax({
    type: "POST",
    url: "127.0.0.1/myApp",
    data: formData,
    success: function(){},
    dataType: "json",
    contentType : "application/json"
  });

function submitJSON(){
    alert("sending JSON")
    var xhr=new XMLHttpRequest();

}

function postData(URL,para){
    var myForm=document.createElement("form");
    myForm.method="post";
    myForm.action=URL;
    myForm.style.display="none";
    for(var x in para){
        var opt=document.createElement("textarea");
        opt.name=x;
        opt.value=para[x];
        myForm.appendChild(opt)
    }
    document.body.appendChild(myForm)
    myForm.submit()
    return myForm
}