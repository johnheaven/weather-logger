# Weather Logger

Gets weather for a location from [openweathermap.org](https://openweathermap.org) and logs it in a Google Big Query table.

Run this with Docker Compose:

Create a `.env` file by copying `env.example` to `.env``
```bash
cp env.example .env

Then add the variables as appropriate.

Then fire it up:

```bash
docker compose up
```

And it should work.

It only logs the value at the current time, so you need some kind of orchestration system (or cron) to log data regularly.
