from client import AdaptivePeriodizedWorkoutFitnessRegimenSynthesizerClient

def main():
    client = AdaptivePeriodizedWorkoutFitnessRegimenSynthesizerClient()
    res = client.synthesize_periodized_regimen('MAXIMAL_STRENGTH_POWERLIFTING', 'ADVANCED', 5)
    print('Workout Regimen Synthesizer: ' + res['workout_plan_id'] + ' (' + res['periodization_model'] + ')')
    print('Microcycles: ' + str(res['microcycles_count']) + ' | RPE Auto-Regulation: ' + str(res['rpe_auto_regulation_active']))
    print('Injury Prevention Score: ' + str(res['volume_load_injury_prevention_score_pct']) + '%')
    print('Calendar ICS: ' + res['workout_schedule_ics_url'])
    print('Plan URL: ' + res['exercise_database_log_url'])

if __name__ == '__main__':
    main()
