const before = document.querySelector('#before-click')
const after = document.querySelector('#after-click')
const editBtn = document.querySelector('#open')

let safePlaces = []

for (let i = 0; i < 20; i++) safePlaces.push(i.toString())

let safeSwitch = false
let arrayOfWatchedTags = []
fetch('/getTag')
    .then(response => response.json())
    .then(result => {
        // this is sending a get request to backend .So we can get some information about our tag table
        // for example tagID is an array which contains current user's id's of watched tags
        arrayOfWatchedTags = result.tagID
        const showCross = (displayType) => {

            arrayOfWatchedTags.forEach(val => {
                document.querySelector(`#tag-${val}`).style.display = displayType
            })

        }

        window.addEventListener('click', (e) => {

            safePlaces.forEach(value => {
                if (e.target.id === value) safeSwitch = true
            })

            if (e.target.id === "watch-tag" || e.target.id === 'open') { // input on

                try {
                    before.style.display = 'none'
                } catch (e) {
                }

                showCross("flex")

                after.style.display = 'flex'
                editBtn.style.display = 'none'

            } else if (safeSwitch) {
                safeSwitch = !safeSwitch
                //safe zone :)

            } else { // input off

                try {
                    before.style.display = 'flex'
                } catch (e) {
                }
                showCross("none")

                after.style.display = 'none'
                editBtn.style.display = 'block'

            }


        })

        arrayOfWatchedTags.forEach(val => {
            document.querySelector(`#tag-${val}`).addEventListener('click', (item) => {

                function getCookie(name) {
                    let cookieValue = null;
                    if (document.cookie && document.cookie !== '') {
                        const cookies = document.cookie.split(';');
                        for (let i = 0; i < cookies.length; i++) {
                            const cookie = cookies[i].trim();
                            // Does this cookie string begin with the name we want?
                            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                break;
                            }
                        }
                    }
                    return cookieValue;
                }

                const csrftoken = getCookie('csrftoken');

                fetch(`/delete/${item.target.id}`,
                    {
                        method: "DELETE",
                        headers: {'X-CSRFToken': csrftoken},
                        mode: 'same-origin' // Do not send CSRF token to another domain.
                    }).then(response => response.json())
                    .then(result => {
                        window.location.href = `/${result.whereTo}`
                    })
                    .catch(e => console.log(e))
            })
        })


    })
    .catch(e => console.log(e))


