const url = new URLSearchParams(window.location.search)

const style = () => {
    try {
        document.querySelector(`#pageButton${url.get('page')}`).style.backgroundColor = "#e7700d"
        document.querySelector(`#pageButton${url.get('page')}`).style.border = "1px solid #e7700d"
        document.querySelector(`#pageButton${url.get('page')}`).href = "javascript: void(0)"
        document.querySelector(`#pageButton${url.get('page')}`).style.cursor = "default"
        document.querySelector(`#pageButton${url.get('page')}`).style.color = "white"
    } catch (e) {
        document.querySelector(`#pageButton1`).style.backgroundColor = "#e7700d"
        document.querySelector(`#pageButton1`).style.border = "1px solid #e7700d"
        document.querySelector(`#pageButton1`).href = "javascript: void(0)"
        document.querySelector(`#pageButton1`).style.cursor = "default"
        document.querySelector(`#pageButton1`).style.color = "white"
    }

    try {
        document.querySelector(`#per${url.get('perPage')}`).style.backgroundColor = "#e7700d"
        document.querySelector(`#per${url.get('perPage')}`).style.border = "1px solid #e7700d"
        document.querySelector(`#per${url.get('perPage')}`).href = "javascript: void(0)"
        document.querySelector(`#per${url.get('perPage')}`).style.cursor = "default"
        document.querySelector(`#per${url.get('perPage')}`).style.color = "white"
    } catch (e) {
        document.querySelector(`#per10`).style.backgroundColor = "#e7700d"
        document.querySelector(`#per10`).style.border = "1px solid #e7700d"
        document.querySelector(`#per10`).href = "javascript: void(0)"
        document.querySelector(`#per10`).style.cursor = "default"
        document.querySelector(`#per10`).style.color = "white"
    }

}

style()

