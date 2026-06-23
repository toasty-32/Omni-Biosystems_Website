from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    supabase_url: str
    supabase_service_role_key: str
    supabase_jwt_secret: str
    environment: str = 'development'
    allowed_origins: str = 'http://localhost:3000'

    @property
    def is_production(self) -> bool:
        return self.environment == 'production'

    @property
    def cors_origins(self) -> list[str]:
        return [o.strip() for o in self.allowed_origins.split(',') if o.strip()]


settings = Settings()  # type: ignore[call-arg]
