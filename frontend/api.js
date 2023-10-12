window.onload = ()=>{
    console.log("loading 되었음!")
}
    

async function handleSignup(){
    const nickname = document.getElementById("nickname").value
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value
    const password2 = document.getElementById("password2").value
    const date_of_birth = document.getElementById("date_of_birth").value
    console.log(email, password)
    
    const response = await fetch('http://127.0.0.1:8000/users/signup/', {
        headers:{
            'content-type':'application/json',
        },
        method:'POST',
        body: JSON.stringify({
            "nickname" : nickname,
            "email": email,
            "password": password,
            "password2": password2,
            "date_of_birth": date_of_birth,
        })
    })
    console.log(response)
    // window.location.replace = "login.html";
}


async function handleLogin(){
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value
    console.log(email, password)

    const response = await fetch('http://127.0.0.1:8000/users/login/', {
        headers:{
            'content-type':'application/json',
        },
        method:'POST',
        body: JSON.stringify({
            "email": email,
            "password": password
        })
    })

    const response_json = await response.json()
    console.log(response_json)

    localStorage.setItem("access", response_json.access);
    localStorage.setItem("refresh", response_json.refresh);

    const base64Url = response_json.access.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function (c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    localStorage.setItem("payload", jsonPayload);
    
    window.location.href = "index.html";
}


function handleLogout(){
    localStorage.removeItem("access")
    localStorage.removeItem("refresh")
    localStorage.removeItem("payload")
}


async function handlePostSubmit(){
    const formData = new FormData();
    const image = document.getElementById("image").files[0]
    const title = document.getElementById("title").value
    const content = document.getElementById("content").value
    const token = localStorage.getItem("access")

    formData.append("image", image)
    formData.append("title", title)
    formData.append("content", content)

    const response = await fetch('http://127.0.0.1:8000/posts/', {
        headers:{
            'Authorization': `Bearer ${token}`
        },
        method:'POST',
        body:formData
    })
    console.log(response)
}