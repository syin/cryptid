import axios from 'axios'
import jsonp from 'jsonp'
import { SHA1, enc } from 'crypto-js'

const apiHost = ''

function capture() {
  const userIdentifier = getUserIdentifier()
  const encryptedUserIdentifier = encryptUserIdentifier(userIdentifier)

  console.log('encryptedUserIdentifier', encryptedUserIdentifier)

  logUserVisit(encryptedUserIdentifier)
}

function getUserIdentifier() {
  const userAgent = navigator.userAgent
  console.log('userAgent', userAgent)

  // jsonp(
  //     'https://api.ipify.org?format=jsonp&callback=?',
  //     undefined,
  //     (err: any, data: any) => {
  //         if (err) {
  //             console.error(err.message)
  //         } else {
  //             console.log(data)
  //         }
  //     }
  // )

  return userAgent
}

function encryptUserIdentifier(input) {
  const hash = SHA1(input)
  const hashString = hash.toString(enc.Base64)
  return hashString
}

function logUserVisit(userIdentifier) {
  const timestamp = new Date().toISOString()
  const currentPage = window.location.pathname
  axios
    .post(`${apiHost}/api/log/`, {
      timestamp: timestamp,
      user: userIdentifier,
      url: currentPage
    })
    .then(response => {
      console.log('return', response)
    })
}

capture()
