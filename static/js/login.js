const signUpButton=document.getElementById("signUp");
const signInButton=document.getElementById("signIn");
const container=document.getElementById("container");
// const pass_confirm=document.getElementById("pass")

signUpButton.addEventListener("click", () => {
    reset();
    container.classList.add('right-panel-active');
});

signInButton.addEventListener("click", () => {
    reset();
    container.classList.remove('right-panel-active');
});

// pass_confirm.addEventListener("click", () => {
//     container.classList.add("pass-page");
// });