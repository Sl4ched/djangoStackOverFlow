//questions
const btNew = document.querySelector('#btNew')
const btActive = document.querySelector('#btActive')
const btBountied = document.querySelector('#btBountied')
const btUnanswered = document.querySelector('#btUnanswered')
const btFilter = document.querySelector('#btFilter')

//tags
const btPopular = document.querySelector('#btPopular')
const btName = document.querySelector('#btName')
const btNew2 = document.querySelector('#btNew2')

//users
const btReputation = document.querySelector('#btReputation')
const btNewUsers = document.querySelector('#btNewUsers')
const btVoters = document.querySelector('#btVoters')
const btEditors = document.querySelector('#btEditors')
const btModerators = document.querySelector('#btModerators')

//home
const btInteresting = document.querySelector('#btInteresting')
const btBountied2 = document.querySelector('#btBountied2')
const btHot = document.querySelector('#btHot')
const btWeek = document.querySelector('#btWeek')
const btMonth = document.querySelector('#btMonth')


const searchParams = new URLSearchParams(window.location.search);

switch (searchParams.get('filter')) {
    case 'newest':
        btNew.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:7px 0 0 7px'
        break
    case 'active':
        btActive.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:0'
        break
    case 'bountied':
        btBountied.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:0'
        break
    case 'unanswered':
        btUnanswered.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:0 7px 7px 0'
        break

    case 'popular':
        btPopular.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:0'
        break
    case 'name':
        btName.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:0'
        break
    case 'new':
        btNew2.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:0 7px 7px 0'
        break

    case 'reputation':
        btReputation.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:7px 0 0 7px'
        break
    case 'newuser':
        btNewUsers.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:0'
        break
    case 'voters':
        btVoters.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:0'
        break
    case 'editors':
        btEditors.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:0'
        break
    case 'moderators':
        btModerators.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:0'
        break

    case 'interesting':
        btInteresting.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:7px 0 0 7px'
        break
    case 'bountied2':
        btBountied2.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:0'
        break
    case 'hot':
        btHot.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:0'
        break
    case 'week':
        btWeek.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:0'
        break
    case 'month':
        btMonth.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:0'
        break

    default:
        // this is for default filter case. if there is no any query parameter first button must be in active state
        // in that case we don't know which page's first button so try and catch blocks try for each page's first button
        try {
            btNew.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:7px 0 0 7px'
        } catch (e) {
            try {
                btPopular.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:0'
            } catch (e) {
                try {
                    btReputation.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:7px 0 0 7px'
                } catch (e) {
                    btInteresting.style = 'background:hsla(0, 0%, 67%, 0.35);border-radius:7px 0 0 7px'
                }
            }
        }

        break
}

