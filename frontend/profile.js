// const backend_base_url = 'http://127.0.0.1:8000'
// const frontend_base_url = 'http://127.0.0.1:5500'

// window.addEventListener('load', async function loadPosts() {
//     profiles = await getProfile()
//     console.log("aaaaa", profiles)

//     fullname.innerText = profiles
//     age.innerText = profiles.age
//     introduce_me.innerText = profiles.introduce_me
//     job.innerText = profiles.job
//     religion.innerText = profiles.religion
//     my_character.innerText = profiles.my_character
//     purpose_to_join.innerText = profiles.purpose_to_join

// }
// )


// async function getProfile() {
//     const token = localStorage.getItem("access")
//     const response = await fetch(`${backend_base_url}/users/${user_id}/profile/`, {
//         headers: {
//             'content-type': 'application/json',
//             'Authorization': `Bearer ${token}`
//         },
//         method: 'GET',
//     })
//     console.log(response)
//     if (response.status == 200) {
//         const response_json = await response.json()
//         return response_json
//     } else {
//         alert("불러오는데 실패했습니다.")
//     }
// }


// async function moveToOtherProfile() {

//     posts = await getPosts()

//     let button = document.getElementById("intro2")
//     let nickname = button.innerHTML
//     let user_id = 0;

//     for (let i = 0; i < posts.length; i++) {
//         console.log(posts[i].nickname);
//         if (posts[i].nickname == nickname){
//             user_id = posts[i].user
//         }
//     }

//     const formData = new FormData();
//     const token = localStorage.getItem("access")

//     formData.append("user_id", user_id)

//     const response = await fetch(`http://127.0.0.1:8000/users/${user_id}/profile/`, {
//         headers:{
//             'Authorization': `Bearer ${token}`
//         },
//         method:'GET',
//     })
//     console.log(response)
//     window.location.href = "otherprofile.html";
// }