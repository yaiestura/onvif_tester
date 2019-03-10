from onvif import ONVIFCamera
import random, string

class MediaTests:
	def __init__(self, cam):
		self.cam = cam

	def CreateProfile(self):
		media = self.cam.create_media_service()
		token = media.GetProfiles()[0]._token
		token1 = media.GetProfiles()[-1]._token
		create = media.CreateProfile({'Name': 'Test', 'ProfileToken': token})
		token2 = media.GetProfiles()[-1]._token
		if (token1 != token2):
			delete = media.DeleteProfile({'ProfileToken': token2})
			return 'CreateProfile works', create
		else:
			return 'DeleteProfile does not work', create

	def GetProfiles(self):
		media = self.cam.create_media_service()
		profiles = media.GetProfiles()
		if (len(profiles) > 0):
			return 'GetProfiles works', profiles
		else:
			return 'GetProfiles does not work', profiles

	def GetUri(self):
		media = self.cam.create_media_service()
		token = media.GetProfiles()[0]._token
		uri = media.GetSnapshotUri({'ProfileToken': token})
		if (len(uri)>0):
			return 'GetUri works', uri
		else:
			return 'GetUri does not work', uri

	def DeleteProfile(self):
		media = self.cam.create_media_service()
		token = media.GetProfiles()[0]._token
		token1 = media.GetProfiles()[-1]._token
		media.CreateProfile({'Name': 'Test', 'ProfileToken': token})
		token2 = media.GetProfiles()[-1]._token
		if (token1 != token2):
			delete = media.DeleteProfile({'ProfileToken': token2})
			return 'DeleteProfile works', delete
		else:
			return 'DeleteProfile does not work', delete

	def AddAudioDecoderConfiguration(self):
		media = self.cam.create_media_service()
		token = media.GetProfiles()[0]._token
		create = media.CreateProfile({'Name': 'Test', 'ProfileToken': token})
		token = media.GetProfiles()[-1]._token
		try:
			audio_token = media.GetProfiles()[0].AudioDecoderConfiguration._token
		except AttributeError:
			delete = media.DeleteProfile({'ProfileToken': token})
			return 'AddAudioDecoderConfiguration does not work, AttributeError'
		add_config = media.AddAudioDecoderConfiguration({'ProfileToken': token, 'ConfigurationToken':audio_token})
		audio_token2 = media.GetProfiles()[-1].AudioDecoderConfiguration._token
		delete = media.DeleteProfile({'ProfileToken': token})
		if (audio_token == audio_token2):
			return 'AddVideoSourceConfiguration works', add_config
		else:
			return 'AddVideoSourceConfiguration does not work', add_config

	def AddVideoSourceConfiguration(self):
		media = self.cam.create_media_service()
		token0 = media.GetProfiles()[0]._token
		create = media.CreateProfile({'Name': 'Test', 'ProfileToken': token0})
		token = media.GetProfiles()[-1]._token
		source_token = media.GetProfiles()[0].VideoSourceConfiguration._token  #'vscname_7'
		addvid = media.AddVideoSourceConfiguration({'ProfileToken': token, 'ConfigurationToken':source_token})
		source_token2 = media.GetProfiles()[-1].VideoSourceConfiguration._token
		delete = media.DeleteProfile({'ProfileToken': token})
		if (source_token == source_token2):
			return 'AddVideoSourceConfiguration works', addvid
		else:
			return 'AddVideoSourceConfiguration does not work', addvid
				
	def GetVideoSourceConfiguration(self):
		media = self.cam.create_media_service()
		config_token = media.GetProfiles()[0].VideoSourceConfiguration._token
		config = media.GetVideoSourceConfiguration({'ConfigurationToken': config_token})
		if (len(config)>0):
			return 'GetVideoSourceConfiguration works', config
		else:
			return 'GetVideoSourceConfiguration does not work', config


	def GetAudioDecoderConfigurations(self):
		media = self.cam.create_media_service()
		try:
			configs = media.GetAudioDecoderConfigurations()
			token = configs[0]._token
		except AttributeError:
			return 'GetAudioDecoderConfigurations does not work, AttributeError', configs
		return 'GetAudioDecoderConfigurations works', configs
			

	def GetAudioOutputConfigurations(self):
		media = self.cam.create_media_service()
		configs = media.GetAudioOutputConfigurations()
		if (len(configs)>0):
			return 'GetAudioOutputConfigurations works', configs
		else:
			return 'GetAudioOutputConfigurations does not work', configs
