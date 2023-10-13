window.addEventListener('load', function () {
    const payload = localStorage.getItem("payload");
    const payload_parse = JSON.parse(payload)
    // console.log(payload_parse.email)

    const intro = document.getElementById("intro")
    intro.innerText = payload_parse.email    
})



window.addEventListener('load', async function loadPosts() {
    posts = await getPosts()
    console.log(posts)
    intro2.innerText = posts[4].nickname
}
)


function openCloseToc() {
    if (document.getElementById('toc-content').style.display === 'block') {
        document.getElementById('toc-content').style.display = 'none';
        document.getElementById('toc-toggle').textContent = '댓글 보기';
    } else {
        document.getElementById('toc-content').style.display = 'block';
        document.getElementById('toc-toggle').textContent = '숨기기';
    }
}

async function loadProfileData() {
    const response = await fetchApi(`${backend_base_url}/users/my_profile/`, 'GET');
    if (response) {
        document.getElementById("fullname").value = response.fullname || '';
        document.getElementById("age").value = response.age || '';
        document.getElementById("introduce_me").value = response.introduce_me || '';
        document.getElementById("job").value = response.job || '';
        document.getElementById("religion").value = response.religion || '';
        document.getElementById("my_character").value = response.my_character || '';
        document.getElementById("purpose_to_join").value = response.purpose_to_join || '';
    }
}

async function handleProfileSubmit() {
    const fullname = document.getElementById("fullname").value;
    const age = document.getElementById("age").value;
    const introduce_me = document.getElementById("introduce_me").value;
    const job = document.getElementById("job").value;
    const religion = document.getElementById("religion").value;
    const my_character = document.getElementById("my_character").value;
    const purpose_to_join = document.getElementById("purpose_to_join").value;

    const formData = {
        fullname,
        age,
        introduce_me,
        job,
        religion,
        my_character,
        purpose_to_join
    };

    const response = await fetchApi(`${backend_base_url}/users/my_profile/`, 'POST', formData);

    if (response) {
        alert("프로필이 성공적으로 저장되었습니다.");
    } else {
        alert("프로필 저장에 실패했습니다. 다시 시도해 주세요.");
    }
}
