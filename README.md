```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Sujan Portfolio</title>

  <style>
    *{
      margin:0;
      padding:0;
      box-sizing:border-box;
      scroll-behavior:smooth;
      font-family: Arial, Helvetica, sans-serif;
    }

    body{
      background:#0f172a;
      color:white;
    }

    header{
      width:100%;
      padding:20px 10%;
      display:flex;
      justify-content:space-between;
      align-items:center;
      position:fixed;
      top:0;
      background:#0f172a;
      z-index:1000;
      border-bottom:1px solid #1e293b;
    }

    .logo{
      font-size:28px;
      font-weight:bold;
      color:#38bdf8;
    }

    nav a{
      color:white;
      text-decoration:none;
      margin-left:25px;
      transition:0.3s;
    }

    nav a:hover{
      color:#38bdf8;
    }

    section{
      min-height:100vh;
      padding:120px 10%;
    }

    .hero{
      display:flex;
      justify-content:space-between;
      align-items:center;
      flex-wrap:wrap;
    }

    .hero-text{
      flex:1;
    }

    .hero-text h1{
      font-size:60px;
      margin-bottom:20px;
    }

    .hero-text span{
      color:#38bdf8;
    }

    .hero-text p{
      font-size:18px;
      line-height:1.7;
      color:#cbd5e1;
      margin-bottom:30px;
      max-width:600px;
    }

    .btn{
      display:inline-block;
      padding:14px 30px;
      background:#38bdf8;
      color:black;
      text-decoration:none;
      border-radius:8px;
      font-weight:bold;
      transition:0.3s;
    }

    .btn:hover{
      transform:scale(1.05);
      background:#0ea5e9;
    }

    .hero-img{
      flex:1;
      text-align:center;
    }

    .hero-img img{
      width:300px;
      border-radius:50%;
      border:5px solid #38bdf8;
      box-shadow:0 0 30px #38bdf8;
    }

    .title{
      text-align:center;
      margin-bottom:50px;
      font-size:40px;
      color:#38bdf8;
    }

    .skills{
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
      gap:20px;
    }

    .skill-card{
      background:#1e293b;
      padding:30px;
      border-radius:12px;
      text-align:center;
      transition:0.3s;
    }

    .skill-card:hover{
      transform:translateY(-10px);
      background:#334155;
    }

    .projects{
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
      gap:25px;
    }

    .project-card{
      background:#1e293b;
      padding:25px;
      border-radius:15px;
      transition:0.3s;
    }

    .project-card:hover{
      transform:scale(1.03);
    }

    .project-card h3{
      margin-bottom:15px;
      color:#38bdf8;
    }

    .project-card p{
      color:#cbd5e1;
      line-height:1.6;
    }

    .contact{
      text-align:center;
    }

    .contact p{
      margin:15px 0;
      color:#cbd5e1;
      font-size:18px;
    }

    footer{
      text-align:center;
      padding:20px;
      background:#020617;
      color:#94a3b8;
    }

    @media(max-width:900px){

      .hero{
        flex-direction:column-reverse;
        text-align:center;
      }

      .hero-text h1{
        font-size:45px;
      }

      .hero-img{
        margin-bottom:40px;
      }

      nav{
        display:none;
      }
    }

  </style>
</head>
<body>

  <header>
    <div class="logo">Sujan.</div>

    <nav>
      <a href="#home">Home</a>
      <a href="#skills">Skills</a>
      <a href="#projects">Projects</a>
      <a href="#contact">Contact</a>
    </nav>
  </header>

  <!-- HOME -->
  <section class="hero" id="home">

    <div class="hero-text">
      <h1>Hello, I'm <span>Sujan</span></h1>

      <p>
        Python Developer | Web Developer | Problem Solver
        
        I build clean and modern projects using Python,
        HTML, CSS, JavaScript, and GitHub.
      </p>

      <a href="https://github.com/" class="btn" target="_blank">
        Visit GitHub
      </a>
    </div>

    <div class="hero-img">
      <img src="https://i.pravatar.cc/300" alt="profile">
    </div>

  </section>

  <!-- SKILLS -->
  <section id="skills">

    <h2 class="title">Skills</h2>

    <div class="skills">

      <div class="skill-card">
        <h3>Python</h3>
      </div>

      <div class="skill-card">
        <h3>HTML</h3>
      </div>

      <div class="skill-card">
        <h3>CSS</h3>
      </div>

      <div class="skill-card">
        <h3>JavaScript</h3>
      </div>

      <div class="skill-card">
        <h3>Git & GitHub</h3>
      </div>

      <div class="skill-card">
        <h3>OOP</h3>
      </div>

    </div>

  </section>

  <!-- PROJECTS -->
  <section id="projects">

    <h2 class="title">Projects</h2>

    <div class="projects">

      <div class="project-card">
        <h3>QR Code Generator</h3>

        <p>
          Python project that generates QR codes
          using qrcode and Pillow library.
        </p>
      </div>

      <div class="project-card">
        <h3>Student Management System</h3>

        <p>
          OOP based Python application for managing
          student records and marks.
        </p>
      </div>

      <div class="project-card">
        <h3>Portfolio Website</h3>

        <p>
          Responsive personal portfolio website
          using HTML and CSS.
        </p>
      </div>

    </div>

  </section>

  <!-- CONTACT -->
  <section class="contact" id="contact">

    <h2 class="title">Contact Me</h2>

    <p>Email: sujan@example.com</p>

    <p>GitHub: github.com/yourusername</p>

    <p>Location: Nepal</p>

  </section>

  <footer>
    © 2026 Sujan Portfolio | All Rights Reserved
  </footer>

</body>
</html>
```
