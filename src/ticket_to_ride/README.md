# Ticket to Ride Europe Analysis
<h2>Intro</h2>
Ticket to Ride Europe(TTRE) is a multiplayer board game where players use matching Train Cards to build railway routes between cities to earn the most points.
<br/>
This analysis aims to inform players's decision-making by illustrating to what degree claiming routes and completing Destination Tickets can maximize their points earned per Train Card used.</br>

<h2>Claiming Routes</h2>
<h3>Route Length</h3>
In TTRE, players exchange Train Cards to claim routes with a 1 to 1 exchange rate. However, players will earn more points for claiming longer routes. This means that it is more point efficient to use Train Cards on longer routes.</br>

<img src="../../images/ttre/PointsPerRoute0.png" width="500" height="250"></br>
<img src="../../images/ttre/PointsPerRouteRatio0.png" width="500" height="250"></br>
From this observation, a player may notice that a simple strategy to use in TTRE is to claim the longest routes as quickly as possible because they give the most points per Train Card.</br>

<h3>Route Colors</h3>
Train Routes in TTRE come in 9 different colors: 8 Main Colors (Green, Blue, White, Purple, Black, Red, Orange, Yellow) and 1 "Wild" Color (Gray). We first see which color of routes yield the most total points.</br>

<img src="../../images/ttre/MainColorPoints0.png" width="500" height="250"></br>
<img src="../../images/ttre/AllColorPoints0.png" width="500" height="250"></br>
Green/Blue have the most potential points out of the Main Colors, while Orange/Yellow have the least potential points. However, both pale in comparison to the total potential points that the Gray routes offer.</br>
We look at why this is the case in this breakdown of the routes.</br>

<img src="../../images/ttre/ColorTable.png" width="800" height="250"></br>

This table suggests that the colors that yield the most points are generally the ones with the most longest routes (E.g. Green/Blue have the most length 4 routes out of the Main Colors, so they yield more points than the other Main Colors).</br>

Since players will be holding cards throughout the game, holding the higher value Green/Blue Train Cards may give players a better chance to claim longer routes while denying other players from getting them.</br>

<h2>Destination Tickets</h2>
<h3>Ticket Efficiency</h3>
Instead of focusing on which Destination Tickets give the most points, we want to know which Destination Tickets give the most points per Train Card used.</br>

We measure the value of Destination Tickets by taking the (Destination Ticket Points + Points per Route Length) / (Route Length). To calculate the Points per Route Length for each Destination Ticket, we assume the Route Length is the shortest possible path from city A to city B on the Destination Ticket <a href="https://boardgamegeek.com/thread/339111/ttr-europe-ticket-analysis">(Credits to gunnarorn for compiling this information)</a>.</br>

<img src="../../images/ttre/DestinationTicketHistogram.png" width="1200" height="250"></br>

The first observation is that Destination Tickets make routes very point efficient. All Destination Tickets have a greater than 2 Points per Route Length Ratio. This means that all routes of length <=4 that contribute to a Destination Ticket are more point efficient than a standalone route of length 4.</br>

The next observation is the outlier in the [3.1, 3.2] bin, the 'Palermo to Constantinople' Destination Ticket. This is the only ticket to utilize a route of length >4 in its shortest path (it uses a length 6 route), making it very point efficient.</br>

We look at a table of the top 20 most efficient Destination Tickets.</br>

<img src="../../images/ttre/Top20Tickets.png" width="300" height="300"></br>

Here we see that the Top 11 Destination Tickets upon completion make the routes that were used to complete them as efficient as standalone length 6 routes. Additionally, we notice that the Top 20 Destination Tickets all incorporate at least 1 length 4 route in their shortest route path.</br>

One possible strategy that arises from this observation is to complete as many high value Destination Tickets as soon as possible.</br>

<h2>Conclusion</h2>
From this analysis, the takeaway is that the length 8 route, the 2 length 6 routes, and Destination Tickets with at least 1 length 4 route in its shortest path are high value objectives to claim while playing TTRE because they maximize a player's points per Train Card used. Additionally, two basic strategies arose from this analysis: claiming longest routes and completing point efficient Destination Tickets.</br>

In the future, it would be interesting to discuss which strategy is appropriate for what situations as both have pros and cons. With the longest route strategy, players are not claiming routes frequently, but they are turn-efficient; that is, they use many Train Cards in a single turn for the most amount of points. With the Destination Tickets, players make shorter routes more point efficient, but they take more turns to use the same amount of Train Cards for a similar amount of points. The question then is if the longest route strategy is better because it causes the game to finish more quickly? Another dimension to look into would be how each strategy is affected with a different number of players.</br>

TTRE is one of those easy to learn but hard to master games where it may be that only real game experience may give us the answers.
