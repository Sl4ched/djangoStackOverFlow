const account = document.querySelector('.account')
const dropdownContent = document.querySelector('.dropdown-content')
let bool = ['block', 'none']
let sw = true
account.addEventListener('click', () => {
    sw ? dropdownContent.style.display = bool[0] : dropdownContent.style.display = bool[1]
    sw = !sw
})
