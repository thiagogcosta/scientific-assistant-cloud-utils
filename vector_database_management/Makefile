create-chroma-db:
	@aws cloudformation create-stack --stack-name my-chroma-stack --template-url https://s3.amazonaws.com/public.trychroma.com/cloudformation/latest/chroma.cf.json --parameters ParameterKey=ChromaServerAuthCredentials,ParameterValue="chr0ma-t0k3n" ParameterKey=ChromaServerAuthProvider,ParameterValue="chromadb.auth.token_authn.TokenAuthenticationServerProvider" ParameterKey=ChromaAuthTokenTransportHeader,ParameterValue="Authorization" ParameterKey=InstanceType,ParameterValue=t3.nano
	
delete-chroma-db:
	@aws cloudformation delete-stack --stack-name my-chroma-stack
