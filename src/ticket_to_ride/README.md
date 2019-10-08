# Ticket to Ride Europe Analysis
<h2>Intro</h2>
Ticket to Ride Europe(TTRE) is a multiplayer board game where players use matching Train Cards to build railway routes between cities to earn the most points.</br>
This analysis aims to inform players's decision-making by illustrating to what degree claiming routes and completing Destination Tickets can maximize their points earned per Train Card used.

<h2>Claiming Routes</h2>
<h3>Route Length</h3>
In TTRE, players will earn more points for claiming longer routes, making it more efficient to use Train Cards on longer routes.</br>
![PointsPerRoute](../../images/ttre/PointsPerRoute.png)
![PointsPerRouteRatio](../../images/ttre/PointsPerRouteRatio.png)
From this observation, a player may notice that a simple strategy is to claim the longest routes ASAP.</br>
<h3>Route Colors</h3>
Train Routes come in 9 different colors: 8 Main Colors (Green, Blue, White, Purple, Black, Red, Orange, Yellow) and 1 "Wild" Color (Gray). We first see which color of routes yield the most total points.
![AllColorPoints](../../images/ttre/AllColorPoints.png)
![MainColorPoints](../../images/ttre/MainColorPoints.png)
We see that Green/Blue are the colors that have the most potential points out of the main colors, while Orange/Yellow have the least potential points. However, both pale in comparison to the total potential points that the Gray routes offer.</br>
We can  look at why this is the case in this breakdown of the routes.
![ColorTable](../../images/ttre/ColorTable.png)
