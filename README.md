<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Programming Problems Website - README</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

  body {
    font-family: 'Inter', sans-serif;
    background: #f0f4f8;
    color: #222;
    margin: 0;
    padding: 2rem;
    display: flex;
    justify-content: center;
  }
  main {
    background: #fff;
    max-width: 900px;
    width: 100%;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    padding: 3rem 4rem;
    line-height: 1.6;
  }
  h1 {
    color: #2c3e50;
    font-weight: 700;
    margin-bottom: 1rem;
    border-bottom: 3px solid #3498db;
    padding-bottom: 0.5rem;
  }
  h2 {
    color: #34495e;
    margin-top: 2.5rem;
    margin-bottom: 1rem;
    font-weight: 600;
  }
  p {
    font-size: 1.1rem;
  }
  ul, ol {
    margin-left: 1.5rem;
    font-size: 1.05rem;
  }
  li {
    margin-bottom: 0.7rem;
  }
  pre {
    background-color: #272822;
    color: #f8f8f2;
    padding: 1rem 1.5rem;
    border-radius: 8px;
    overflow-x: auto;
    font-family: 'Source Code Pro', monospace, monospace;
    font-size: 0.95rem;
    box-shadow: inset 0 0 5px rgba(0,0,0,0.5);
    margin: 0.8rem 0;
  }
  code {
    background-color: #eee;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: monospace;
    font-size: 0.95rem;
  }
  ol li pre {
    margin-top: 0.4rem;
    margin-bottom: 0.8rem;
  }
</style>
</head>
<body>
  <main>
    <h1>Programming Problems Website</h1>

    <p>A web application to manage programming problems and solutions with user authentication, the ability to share problems via email, and saving information securely.</p>

    <h2>Features</h2>
    <ul>
      <li><strong>User Login:</strong> Secure authentication system for users to access their accounts.</li>
      <li><strong>Save Information:</strong> Users can create and save programming problems and their solutions.</li>
      <li><strong>Send to Email:</strong> Share programming problems via email directly from the app.</li>
    </ul>

    <h2>Project Overview</h2>
    <p>This website allows users to register and log in, create programming problems along with solutions, save them in the database, and share any problem by sending it to an email address. It’s designed to help programmers organize problems and collaborate by sharing easily.</p>

    <h2>Installation</h2>
    <ol>
      <li>Clone the repository:
        <pre><code>git clone &lt;your-repo-url&gt;
cd &lt;your-project-folder&gt;</code></pre>
      </li>
      <li>Install dependencies:
        <pre><code>npm install</code></pre>
      </li>
      <li>Configure environment variables (for example, MongoDB URI, JWT secret, email credentials).</li>
      <li>Start the server:
        <pre><code>npm start</code></pre>
      </li>
    </ol>

    <h2>Usage</h2>
    <ul>
      <li>Register or log in to your account.</li>
      <li>Add new programming problems and solutions.</li>
      <li>View your saved problems.</li>
      <li>Send problems to an email address for sharing or collaboration.</li>
    </ul>

    <h2>Technologies Used</h2>
    <ul>
      <li>Node.js with Express (Backend)</li>
      <li>MongoDB (Database)</li>
      <li>JWT (Authentication)</li>
      <li>Nodemailer (Email sending)</li>
    </ul>

    <h2>Future Improvements</h2>
    <ul>
      <li>Frontend UI with React or Vue.js.</li>
      <li>More advanced user roles and permissions.</li>
      <li>Problem categories and tags.</li>
      <li>Code editor integration.</li>
    </ul>
  </main>
</body>
</html>
