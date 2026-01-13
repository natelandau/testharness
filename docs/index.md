# Valentina Noir

![Valentina Noir](https://cdn.valentina-noir.com/assets/valentina512.png)

A comprehensive API for managing World of Darkness games.

## Features

-   Support for v4 and v5 of the World of Darkness system
-   Full support for vampires, werewolves, hunters, and mortals. Basic support for mages.
-   Dicerolling and gameplay mechanics
-   Character auto-generation
-   Storyteller NPC and character creation
-   Campaign and story tracking
-   Configurable dictionary of game terms and concepts
-   Multi-tenant support
-   Statistics and analytics
-   Settings to configure gameplay and rulesets

## Core Concepts

-   **Company** - A company contains many users, campaigns, and characters. Companies are the top level entity in Valentina Noir and each API key is associated with a single company. Valentina is fully federated and each company is a distinct entity.
-   **Developer** - A developer is an individual who is granted an API key to access the Valentina Noir API for a specific company. Developers may build any number of applications that use the Valentina Noir API.
-   **User** - A user is an individual who is associated with a role within a company. These roles are:
    -   **Admin** - An admin is a user who has full access to all information in a company. Admins are able to manage users and company settings. They also have all permissions granted to Storytellers.
    -   **Storyteller** - Storytellers are able to manage campaigns, characters, grant experience, and any other aspect of the game that is not related to the company's settings.
    -   **Player** - A player is a user who can create and manage their own characters and participate in the game.
-   **Campaign** - A campaign is a distinct world which can contain many story arcs, characters, and span multiple time periods.
-   **Book** - A book is a singular theme or storyline within a campaign.
-   **Chapter** - A chapter is an individual gaming session within a book.
-   **Character** - A character is a player or NPC in a campaign.
-   **Trait** - A trait is a character's ability or attribute.
-   **Concept** - A concept is a character's background or personality.

## Roadmap

The following features are planned for the future:

-   Loresheets
-   Full mage support

## Getting Started

1. [Create an account](https://valentina.dev/signup)
2. [Generate API credentials](https://valentina.dev/settings/api)
3. Authenticate using the `/oauth/token` endpoint
4. Start making requests!

## Support

-   📧 Email: support@valentina-noir.com
-   💬 Discord: [Join our community](https://discord.gg/valentina-noir)
-   📖 Docs: https://docs.valentina-noir.com
