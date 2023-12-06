const account = document.querySelector('.account')
const dropdownContent = document.querySelector('.dropdown-content')
let sw = true
account.addEventListener('click', () => {
    sw ? dropdownContent.style.display = 'block' : dropdownContent.style.display = 'none'
    sw = !sw
})
