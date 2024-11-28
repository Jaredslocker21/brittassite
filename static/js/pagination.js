document.addEventListener("DOMContentLoaded", function () {
    const posts = document.querySelectorAll(".blog-post");
    const pagination = document.getElementById("pagination");
    const postsPerPage = 3;
    let currentPage = 1;

    function renderPosts(page) {
        const start = (page - 1) * postsPerPage;
        const end = start + postsPerPage;

        posts.forEach((post, index) => {
            post.style.display = index >= start && index < end ? "flex" : "none";
        });
    }

    function renderPagination() {
        const totalPages = Math.ceil(posts.length / postsPerPage);
        pagination.innerHTML = "";

        for (let i = 1; i <= totalPages; i++) {
            const pageItem = document.createElement("li");
            pageItem.className = `page-item ${i === currentPage ? "active" : ""}`;
            pageItem.innerHTML = `<a class="page-link" href="#">${i}</a>`;
            pageItem.addEventListener("click", () => {
                currentPage = i;
                renderPosts(currentPage);
                renderPagination();
            });
            pagination.appendChild(pageItem);
        }
    }

    renderPosts(currentPage);
    renderPagination();
});
