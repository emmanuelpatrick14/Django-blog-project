from django.shortcuts import render

# Create your views here.
from datetime import date


all_posts = [
    {
        "slug": "introduction-to-python",
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg",
        "author": "John Doe",
        "date": date(2024, 1, 15),
        "title": "Introduction to Python",
        "excerpt": "A beginner’s guide to the world of Python programming.",
        "content": (
            "Python is a popular programming language known for its simplicity and readability. "
            "In this post, we'll cover the basics of Python and why it's a great choice for both beginners and professionals. "
            "Python is widely used in various domains, from web development and data analysis to artificial intelligence and scientific computing. "
            "One of Python's strengths is its comprehensive standard library, which provides tools suited to many tasks. "
            "Furthermore, the Python community is large and vibrant, providing extensive support and a wealth of resources for developers at all levels. "
            "Python's syntax is designed to be intuitive and mirrors natural language, making it an excellent language for beginners."
            " Its versatility also means that as you advance, you can easily shift focus areas without needing to learn a new language."
        )
    },
    {
        "slug": "advanced-javascript",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png",
        "author": "Jane Smith",
        "date": date(2024, 2, 20),
        "title": "Advanced JavaScript Techniques",
        "excerpt": "Take your JavaScript skills to the next level with these advanced techniques.",
        "content": (
            "JavaScript is a versatile language used in web development. In this post, we'll explore some advanced "
            "techniques to enhance your coding skills and create more dynamic web applications. "
            "We'll delve into concepts like asynchronous programming with promises and async/await, "
            "which allow for cleaner and more manageable asynchronous code. Additionally, we will cover advanced array manipulation, "
            "leveraging methods like map, filter, and reduce to write concise and efficient code. "
            "Another key area we'll focus on is the use of modern JavaScript features introduced in ES6 and beyond, "
            "such as arrow functions, destructuring, and template literals, which can significantly improve code readability and maintainability. "
            "Finally, we'll discuss how to effectively manage state and data flow in complex applications using state management tools like Redux."
        )
    },
    {
        "slug": "css-tricks",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d5/CSS3_logo_and_wordmark.svg",
        "author": "Emily Johnson",
        "date": date(2024, 3, 12),
        "title": "CSS Tricks and Tips",
        "excerpt": "Learn how to make your websites look stunning with these CSS tricks.",
        "content": (
            "CSS is the language that gives style to web pages. This post will share some lesser-known CSS tricks "
            "that can help you create visually appealing and responsive designs. "
            "We will explore the use of CSS variables to create dynamic and reusable styles across your projects. "
            "Moreover, we'll look into advanced layout techniques, such as using Flexbox and CSS Grid, "
            "which enable you to build complex and adaptive layouts with ease. "
            "We'll also discuss how to implement animations and transitions to add life to your web pages, "
            "and how to optimize your CSS for better performance and maintainability. "
            "Lastly, we will touch on accessibility considerations, ensuring that your CSS not only looks good but also provides a great experience for all users."
        )
    },
    {
        "slug": "data-science-intro",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Matplotlib_logo.svg/1200px-Matplotlib_logo.svg.png",
        "author": "Michael Brown",
        "date": date(2024, 4, 18),
        "title": "Introduction to Data Science",
        "excerpt": "Discover the exciting field of data science and its applications.",
        "content": (
            "Data science is a growing field that combines statistics, programming, and domain expertise. "
            "In this post, we'll introduce the basics of data science and discuss its impact on various industries. "
            "We'll start by defining what data science is and how it differs from other related fields like data analysis and machine learning. "
            "Then, we'll explore the data science process, from data collection and cleaning to modeling and visualization. "
            "We'll highlight the importance of choosing the right tools and techniques for the job, "
            "and how to interpret and communicate the results effectively. "
            "Additionally, we'll look at real-world applications of data science, such as predicting customer behavior, "
            "optimizing supply chains, and uncovering new insights in healthcare and finance. "
            "Finally, we'll discuss the ethical considerations of data science, including data privacy and algorithmic bias."
        )
    }
]



def get_date(date):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts,
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts,
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html',{
        'post': identified_post
    })
