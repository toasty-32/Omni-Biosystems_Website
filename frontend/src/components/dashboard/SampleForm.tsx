import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { z } from 'zod'
import { zodResolver } from '@hookform/resolvers/zod'
import { useMutation, useQueryClient } from '@tanstack/react-query'
import { api } from '../../lib/api'

const schema = z.object({
  name: z.string().min(1, 'Name is required'),
  type: z.string().min(1, 'Type is required'),
  collected_at: z.string().min(1, 'Collection date is required'),
})

type FormData = z.infer<typeof schema>

const SAMPLE_TYPES = ['Blood', 'Tissue', 'Urine', 'Saliva', 'Fluid', 'Other']

interface SampleFormProps {
  onSuccess: () => void
}

export default function SampleForm({ onSuccess }: SampleFormProps) {
  const [error, setError] = useState<string | null>(null)
  const queryClient = useQueryClient()

  const { register, handleSubmit, formState: { errors } } = useForm<FormData>({
    resolver: zodResolver(schema),
    defaultValues: { collected_at: new Date().toISOString().slice(0, 10) },
  })

  const mutation = useMutation({
    mutationFn: (data: FormData) =>
      api.post('/samples/', {
        ...data,
        collected_at: new Date(data.collected_at).toISOString(),
      }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['samples'] })
      queryClient.invalidateQueries({ queryKey: ['dashboard-stats'] })
      onSuccess()
    },
    onError: (e: Error) => setError(e.message),
  })

  return (
    <form onSubmit={handleSubmit((d) => mutation.mutate(d))} style={styles.form}>
      <Field label="Sample Name" error={errors.name?.message}>
        <input {...register('name')} placeholder="e.g. Patient-42 Blood Draw" style={styles.input} />
      </Field>
      <Field label="Type" error={errors.type?.message}>
        <select {...register('type')} style={styles.input}>
          <option value="">Select type…</option>
          {SAMPLE_TYPES.map((t) => (
            <option key={t} value={t.toLowerCase()}>{t}</option>
          ))}
        </select>
      </Field>
      <Field label="Collection Date" error={errors.collected_at?.message}>
        <input type="date" {...register('collected_at')} style={styles.input} />
      </Field>
      {error && <p style={styles.error}>{error}</p>}
      <button type="submit" disabled={mutation.isPending} style={styles.button}>
        {mutation.isPending ? 'Saving…' : 'Create Sample'}
      </button>
    </form>
  )
}

function Field({ label, error, children }: { label: string; error?: string; children: React.ReactNode }) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '0.25rem' }}>
      <label style={styles.label}>{label}</label>
      {children}
      {error && <span style={styles.error}>{error}</span>}
    </div>
  )
}

const styles: Record<string, React.CSSProperties> = {
  form: { display: 'flex', flexDirection: 'column', gap: '1rem' },
  label: { fontSize: '0.875rem', fontWeight: 500 },
  input: {
    padding: '0.5rem 0.75rem',
    border: '1px solid var(--color-border)',
    borderRadius: 'var(--radius)',
    fontSize: '0.95rem',
    background: 'var(--color-surface)',
  },
  error: { color: 'var(--color-error)', fontSize: '0.8rem' },
  button: {
    marginTop: '0.5rem',
    padding: '0.625rem 1.25rem',
    background: 'var(--color-primary)',
    color: '#fff',
    border: 'none',
    borderRadius: 'var(--radius)',
    fontSize: '0.95rem',
    fontWeight: 600,
    cursor: 'pointer',
  },
}
