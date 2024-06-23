import scalify
from scalify.settings import (
    AssistantSettings,
    Settings,
    SpeechSettings,
    temporary_settings,
)
from pydantic_settings import SettingsConfigDict


class TestApiKeySetting:
    def test_api_key_initialization_from_env(self, env):
        test_api_key = "test_api_key_123"
        env.set("SCALIFY_OPENAI_API_KEY", test_api_key)

        temp_model_config = SettingsConfigDict(env_prefix="scalify_")
        settings = Settings(model_config=temp_model_config)

        assert settings.openai.api_key.get_secret_value() == test_api_key

    def test_runtime_api_key_override(self, env):
        override_api_key = "test_api_key_456"
        env.set("SCALIFY_OPENAI_API_KEY", override_api_key)

        temp_model_config = SettingsConfigDict(env_prefix="scalify_")
        settings = Settings(model_config=temp_model_config)

        assert settings.openai.api_key.get_secret_value() == override_api_key

        settings.openai.api_key = "test_api_key_789"

        assert settings.openai.api_key.get_secret_value() == "test_api_key_789"


class TestSpeechSettings:
    def test_speech_settings_default(self):
        settings = SpeechSettings()
        assert settings.model == "tts-1-hd"
        assert settings.voice == "echo"
        assert settings.response_format == "mp3"
        assert settings.speed == 1.0


class TestAssistantSettings:
    def test_assistant_settings_default(self):
        settings = AssistantSettings()
        assert settings.model == "gpt-4o"


class TestTemporarySettings:
    def test_temporary_settings_override_and_restore(self, env):
        default_log_level = scalify.settings.log_level

        # for tests it is debug
        assert default_log_level == "DEBUG"

        with temporary_settings(log_level="INFO"):
            assert scalify.settings.log_level == "INFO"

        assert scalify.settings.log_level == default_log_level

    def test_temporary_settings_override_and_restore_nested(self, env):
        default_log_level = scalify.settings.log_level
        initial_api_key = scalify.settings.openai.api_key.get_secret_value()
        default_openai_speech_model = scalify.settings.openai.audio.speech.model

        # for tests
        assert default_log_level == "DEBUG"
        assert initial_api_key.startswith("sk-")
        assert default_openai_speech_model == "tts-1-hd"

        with temporary_settings(
            log_level="INFO",
            openai__api_key="test_api_key",
            openai__audio__speech__model="test_model",
        ):
            assert scalify.settings.log_level == "INFO"
            assert scalify.settings.openai.api_key.get_secret_value() == "test_api_key"
            assert scalify.settings.openai.audio.speech.model == "test_model"

        assert scalify.settings.log_level == default_log_level
        assert scalify.settings.openai.api_key.get_secret_value() == initial_api_key
        assert scalify.settings.openai.audio.speech.model == default_openai_speech_model
