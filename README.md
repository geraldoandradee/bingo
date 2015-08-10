## Bingo

Bingo is a service to provide Bingo cards for its web clients.
It has only one interface that delivers as much card as the client wants.
The default amount of cards is two per request, but clients can request as much as they want.
Check the API for details.

## Tech

The service was built on Python and uses BottlePy (http://bottlepy.org/) to provide the web service.
It is also self-contained into a Docker repository that can be found at:
https://hub.docker.com/r/comdias/bingo-dock/
Project for the Docker Repo:
https://github.com/comdias/bingo-dock

## API

The only API available is the one returning Bingo Cards.

	http://localhost:8080/deal

As default, this interface provides 2 cards per request, but clients can request as much card as they want passing the argument 'cards' to the service and the amount of cards desired.

	http://localhost:8080/deal?cards=5

This will return 5 cards to the client.

### Docker

As mentioned previously, to simplify deployment, the project is available on docker.com.
With this repository image, it is very simple and flexible to deploy Bingo in multiple servers.

#### Bingo Dock

To control the Docker image, there is a git repo available at: https://github.com/comdias/bingo-dock

#### Usage

To use Bingo, you can pull the Docker image to your Docker and run with the following commands:

	$ docker pull comdias/bingo-dock
	$ docker run --rm -p 8080:8080 comdias/bingo-dock

This will let you connect to host port 8080 and receive Bingo cards.

	http://localhost:8080/deal
	http://localhost:8080/deal?cards=10
