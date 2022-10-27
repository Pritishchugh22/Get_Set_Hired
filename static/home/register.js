const userText = document.querySelector(".title-text .user");
const userForm = document.querySelector("form.user");
const userBtn = document.querySelector("label.user");
const companyBtn = document.querySelector("label.company");
const companyLink = document.querySelector("form .company-link a");
companyBtn.onclick = (() => {
    userForm.style.marginLeft = "-50%";
    userText.style.marginLeft = "-50%";
});
userBtn.onclick = (() => {
    userForm.style.marginLeft = "0%";
    userText.style.marginLeft = "0%";
});
companyLink.onclick = (() => {
    companyBtn.click();
    return false;
});
