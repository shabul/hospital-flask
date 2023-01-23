function migrata_alert(title,text,type){
try{
    const rm_toast = document.querySelector(".toasted");
    // console.log(toast1);
    rm_toast.remove();
}
catch(err){
    console.log(err)
};
const toaster = document.createElement('div');
toaster.setAttribute('class','toasted '+type);

const toasted_content=document.createElement('div');
toasted_content.setAttribute("class","toasted-content");

if(type=='success'){
const icon=document.createElement('i');
console.log(type)
icon.setAttribute('class','fas fa-solid fa-check icon-success');
toasted_content.appendChild(icon)
}
else if(type=='warning'){
    const icon=document.createElement('i');
    icon.setAttribute('class','fa-solid fa-exclamation icon-warning');
    toasted_content.appendChild(icon)
}
else if(type=='info'){
    const icon=document.createElement('i');
    icon.setAttribute('class','fa-solid fa-info icon-info');
    toasted_content.appendChild(icon)
}
else if(type=='failed'){
    const icon=document.createElement('i');
    icon.setAttribute('class','fa-solid fa-xmark icon-failed');
    toasted_content.appendChild(icon)
}

const msg=document.createElement('div');
msg.setAttribute('class','message');

const header=document.createElement('span');
header.setAttribute("class","alerttext title-1");

const alert_text=document.createElement('span');
alert_text.setAttribute("class","alerttext msg-2");

const close=document.createElement('i');
close.setAttribute('class','fa-solid fa-xmark close');

const pro=document.createElement('div');
pro.setAttribute('class','progressbar');


//add the new element to html
var body = document.querySelector('body');
// var body=document.getElementById('alert_slide');
body.prepend(toaster);
toaster.appendChild(toasted_content);
toaster.appendChild(close)
toaster.appendChild(pro)
toasted_content.appendChild(msg)
msg.appendChild(header)
msg.appendChild(alert_text)
document.getElementsByClassName('title-1')[0].innerHTML=title;
document.getElementsByClassName('msg-2')[0].innerHTML=text;


const button = document.querySelector("button"),
      toast = document.querySelector(".toasted"),
      closeIcon = document.querySelector(".close"),
      progress = document.querySelector(".progressbar");

      let timer1;

        setTimeout(()=> {
        toast.classList.add("active");
        progress.classList.add("active");
        },1);

        timer1 = setTimeout(() => {
            toast.classList.add("hide");
        },5000); 

      closeIcon.addEventListener("click", () => {
      toast.classList.add("hide");
      
        clearTimeout(timer1);
      });
    
    setTimeout(() => {
    toaster.remove();
    },6000);
    
}