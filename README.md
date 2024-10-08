# Turlink AI Service

## Table of Contents
- [Getting Started](#getting-started)
- [Project Description](#project-description)
- [External APIs and Services](#external-apis-and-services)
- [End Points](#end-points)
- [Contributors](#contributors)
- [FE Repo](https://github.com/turingschool/turlink-fe)
- [BE Repo](https://github.com/turingschool/turlink-be)
- [Deployment](https://nameless-garden-14218-de5663d17d61.herokuapp.com/)

## Getting Started
### Versions
- Python 3.12.5
- Django: 5.1

## Project Description

Turlink AI Service is a micro service of [Turlink](https://turlink-fe-da6763e5d8d6.herokuapp.com/)! This micro service is built in Python 3.12.5 and consumes the openAI API. There is one exposed endpoint that allows for each shorten link to receive a brief AI generated description in a three bullet point format.  

[Turlink](https://turlink-fe-da6763e5d8d6.herokuapp.com/) was designed and built with a team of 8 developers as part of the [Capstone project](https://mod4.turing.edu/projects/capstone/) from Turing School of Software and Design. The Turlink AI Service was built with 2 Backend devlopers from the Capstone project.

<details>
  <summary>Setup</summary>

  1. Fork and/or Clone this Repo from GitHub.

  2. In your terminal use `$ git clone git@github.com:turingschool/turlink-ai-service.git`.

  3. Create a virtual enviorment with `$ python -m venv myenv`

  4. Activate your virtual enviorment with `$ source myenv/bin/activate`

  5. Change into the cloned directory using `$ cd example`.

  6. In your virtual enviorment use `$ pip install django`.

  7. In your virtual enviorment use `$ pip install djangorestframework`.

  8. In your virtual enviorment use `$ pip install requests`.

</details>

<details>
  <summary>Testing</summary>

  Test using the terminal utilizing Unittest:

  `pip install unittest`
  ```bash
  $ python <follow directory path to test specific files>
  ```
</details>


## External APIs and Services
#### OpenAI API
  - In our application, we utilize OpenAI API to produce AI generated prompts for [Turlink](https://turlink-fe-da6763e5d8d6.herokuapp.com/). We're able to acomplish this by exposing the openAI API [chat completions](https://platform.openai.com/docs/api-reference/chat/create) endpoint. Lastly for better readability we format the prompts to be described in 3 bullet points.

  - [OpenAI API Chat Completion Documentation](https://platform.openai.com/docs/guides/chat-completions)


## End Points
### OpenAI
<details>
<summary> Create One Link Description </summary>

Request:

```http
POST /api/v1/openai
Content-Type: application/json
Accept: application/json
```

Body: 

```json
{
  "link": "www.example.com"
}
```

Response: `status: 201`

```json
{
  "data": {
    "link": "www.example.com",
    "summary": "1. example 1\n2. example 2\n3. example 3"
  }
}
```
</details>

### Mock Request
<details>
<summary> Get AI Text </summary>

Request:

```http
GET /api/v1/ping
Content-Type: application/json
Accept: application/json
```

Response: `status: 200`

```json
{
  "data": {
    "link": "www.example.com",
    "summary": "1. example 1\n2. example 2\n3. example 3"
  }
}
```
</details>

## Contributors

* Lance Butler | [GitHub](https://github.com/LJ9332) | [LinkedIn](https://www.linkedin.com/in/lance-butler-jr/)
* Luis Aparicio | [GitHub](https://github.com/LuisAparicio14) | [LinkedIn](https://www.linkedin.com/in/luis-aparicio14/)
