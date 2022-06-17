<div id="top"></div>

<br />

<div align="center">
  <p align="center">
    An awesome project that count words in string and sort it by count in descending order
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- ![Product screenshot](/images/screenshot.jpeg). -->

This project counts words in string and sort it by count in descending order

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With


* [Next.js](https://nextjs.org/) - Frontend
* [FastAPI](https://fastapi.tiangolo.com/) - Backend

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

### Prerequisites

This document assumes that you have already installed prerequisites in the system. if not then please install it from respective website..
* [NodeJs](https://nodejs.org/en/)
* [Python3](https://www.python.org/downloads/)
* [Next.js](https://nextjs.org/)

### Installation

_Below is an example of how you can install and setting up the app._

#### Start Python API Server
1. Go to `backend` folder and create virtual enviroment or you can create interactively in pycharm.
  ```ss
  cd Backend
  python3 -m venv .venv
  ```
2. Activate virtual enviroment.
  ```sh
  source .venv/bin/activate
  ```
3. Install dependencies from `requirements.txt`.
  ```sh
  pip install -r requirements.txt
  ```
4. Start the server.
  ```
  uvicorn main:app --reload
  ```

#### Start Frontend Application
1. Go to frontend folder and install dependencies.
  ```sh
  cd frontend && yarn install
  ```
2. Start the development server.
  ```sh
  yarn dev
  ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

* Go to [http://localhost:3000](http://localhost:3000)
* Enter your string in textarea and click `Count works` button to count words.
* The above method will display output in table below the button.

