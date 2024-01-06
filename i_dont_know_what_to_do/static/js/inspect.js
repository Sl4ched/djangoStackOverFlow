const area = document.querySelector('#text-area')
const comment = document.querySelector('#comment-inspection')


let str = ""
area.addEventListener('input', (e) => {
    e.inputType === "deleteContentBackward" && (str = str.substring(0, str.length - 1))
    e.data !== null && (str += e.data)
    comment.innerText = str
})


