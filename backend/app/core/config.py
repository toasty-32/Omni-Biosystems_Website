from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    supabase_url: str
    supabase_service_role_key: str
    supabase_jwt_secret: str
    environment: str = 'development'

    @property
    def is_production(self) -> bool:
        return self.environment == 'production'


settings = Settings()  # type: ignore[call-arg]
