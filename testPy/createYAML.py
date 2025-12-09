#create a yaml file named config.yaml with some sample configuration data
import yaml

def create_yaml_file(filename):
    config_data = {
        'database': {
            'host': 'localhost',
            'port': 5432,
            'user': 'admin',
            'password': 'password123'
        },
        'audio_id3': {
            'title': 'Sample Song',
            'artist': 'Sample Artist',
            'album': 'Sample Album',
            'year': 2025
        }
    }
    
    with open(filename, 'w') as file:
        yaml.dump(config_data, file)

    # add a sample video ID3 node
    config_data['video_id3'] = {
        'title': 'Sample Video',
        'director': 'Sample Director',
        'codec': 'H.264',
        'resolution': '1920x1080',
        'year': 2024
    }

    with open(filename, 'w') as file:
        yaml.dump(config_data, file)


if __name__ == '__main__':
    output_file = 'config.yaml'
    create_yaml_file(output_file)
    print(f"{output_file} created with sample configuration data.")
